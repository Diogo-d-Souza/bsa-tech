import json
import asyncio

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .utils import fibonacci, send_time
from users.models import User

class BasicConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Establish a connection to the websocket server, adds a user to the room and to the database.
        """
        self.room_name = "datetime_room"
        self.room_group_name = f"users_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.add_user(self.channel_name)

        self.send_task = asyncio.create_task(send_time(self))

    async def disconnect(self, code):
        """
        Ends the connection to the websocket server, removes the user from room and from the database.
        """
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        await self.remove_user(self.channel_name)

    @sync_to_async
    def add_user(self, channel_name):
        """
        Helper function to add the user to database.
        """
        User.objects.create(channel_name=channel_name)

    @sync_to_async
    def remove_user(self, channel_name):
        """
        Helper function to remove the user from database.
        """
        User.objects.filter(channel_name=channel_name).delete()


    async def receive(self, text_data):
        """
        Method that holds the logic to handle the number send by the user and return the fibonacci number.
        """
        try:
            text_data_json = json.loads(text_data)

            n = int(text_data_json.get('n', 0))
            result = fibonacci(n)

            await self.send(text_data=json.dumps({
                'result': result
            }))
        except ValueError as e:
            await self.send(text_data=json.dumps({
                'error': f"Invalid input for Fibonacci: {e}"
            }))