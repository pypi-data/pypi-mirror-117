import asyncio
import collections

import discord
from discord.ext import commands
from discord.abc import Messageable, Typing


FakeResponse = collections.namedtuple("FakeResponse", ["status", "reason"])


class InteractionTyping(Typing):

    async def __aenter__(self):
        return self.__enter__()

    async def do_typing(self, sleep_forever: bool = True):
        if not self.messageable._sent_ack_response and not self.messageable._sent_message_response:
            async with self.messageable._send_interaction_response_lock:
                await self.messageable.defer()
        while sleep_forever:
            await asyncio.sleep(5)  # Loop forever


class InteractionMessageable(Messageable):
    """
    A messageable that allows you to send back responses to interaction payloads
    more easily.

    .. note::

        The interaciton messageable's send method also implements :code:`ephemeral` as a valid kwarg,
        but for ease of documentation, the send method remains undocumented, as aside from this it is
        unchanged from the rest of the messageable objects.

    Attributes:
        component (typing.Optional[BaseComponent]): The component that triggered this interaction.
            It may be none if the interaction that triggered this wasn't a component, such as when
            slash commands are used.
        values (typing.Optional(typing.List[str])): A list of values that were passed through from the component.
    """

    is_interaction = True
    CAN_SEND_EPHEMERAL = True
    ACK_IS_EDITABLE = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._send_interaction_response_lock = asyncio.Lock()  # A lock so we don't try to respond initially twice
        self._send_interaction_response_task = None  # The task for sending an initial "waiting" response
        self._sent_ack_response = False
        self._sent_message_response = False

        self.component = None  # We'll put the interacted-with component here if we get one
        self.values = None

        # If we want to respond before sending a pending response, we can use type 4 - this responds intially with a message.
        #     After doing this we want to respond using webhooks rather than the interaction endpoint.
        # While pending we can send a type 5 response - this means that the interaction gets an ack and goes into a pending state.
        #     After doing this the first time we want to send an initial response again, and followup messages go to the webhook
        #     response endpoint.
        # Buttons have the luxury of a type 6 response - an ack response that doesn't tell the user we're waiting.
        #     Button responses can go immediately to the webhook response endpoint after this ack is received.

    async def _get_channel(self):
        """
        Get the (interaction_id, application_id, token) tuple that's used to send to the webhook necessary.
        """

        return (self.data['id'], self.data['application_id'], self.data['token'],)

    def _send_interaction_response_callback(self):
        """
        Send the original interaction response
        """

        async def send_callback():
            await asyncio.sleep(2)
            try:
                await self.trigger_typing()
            except Exception:
                pass
        self._send_interaction_response_task = self._state.loop.create_task(send_callback())

    async def trigger_typing(self, *args, **kwargs):
        await InteractionTyping(self).do_typing(sleep_forever=False)

    async def ack(self, *args, **kwargs):
        """:meta private:"""
        return await self.defer(*args, **kwargs)

    async def defer(self, *, ephemeral: bool = False, defer_type: int = 5):
        """
        Send an acknowledge payload to Discord for the interaction. The :func:`send` method does this
        automatically if you haven't called it yourself, but if you're doing a time-intensive operation
        (anything that takes longer than 5 seconds to send a response), you may want to send the ack
        yourself so that Discord doesn't discard your interaction.

        Args:
            ephemeral (bool, optional): Whether or not the ack is visible only to the user calling the
                command.
        """

        interaction_id, _, token = await self._get_channel()
        r = discord.http.Route('POST', '/interactions/{interaction_id}/{token}/callback', interaction_id=interaction_id, token=token)
        flags = discord.MessageFlags(ephemeral=ephemeral)
        json = {"type": defer_type}
        if flags:
            json.update({"data": {"flags": flags.value}})
        await self._state.http.request(r, json=json)
        self._sent_ack_response = True

    async def respond(self, *args, **kwargs):
        """
        Send a type 4 response to Discord for the interaction. The :func:`send` method does this for
        you automatically if you use the :code:`wait=False` kwarg.
        """

        return await self.send(*args, wait=False, **kwargs)

    def typing(self, *args, **kwargs):
        return InteractionTyping(self)

    async def fetch_message(self, *args, **kwargs):
        raise Exception("This action is not available for this messagable type.")

    async def pins(self, *args, **kwargs):
        raise Exception("This action is not available for this messagable type.")

    def history(self, *args, **kwargs):
        raise Exception("This action is not available for this messagable type.")


def defer_response(ephemeral: bool = False):
    """
    A "check" that defers the response when called. As checks are run before converters, this will defer
    the response immediately. Useful if your converters run database calls.

    Args:
        ephemeral (bool, optional): Whether or not the defer response should be ephemeral.
    """

    async def predicate(ctx):
        if isinstance(ctx, InteractionMessageable):
            await ctx.defer(ephemeral=ephemeral)
        return True
    return commands.check(predicate)
