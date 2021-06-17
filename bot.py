#!/usr/bin/env python3
"""Jerad Alexander | This Program goes into a group and invites up to 50 people to your destination group """

#standard libraries
import time
import random
import sys

#third party imports
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import UserPrivacyRestrictedError, PeerFloodError, UserNotMutualContactError, UserChannelsTooMuchError
# from telethon.tl.functions.messages import AddChatUserRequest

def main():
    # Defining the need variables
    api_id = '1085156' # Input your api_id here
    api_hash = '8fc35aeb9a10c2bd4948736232da8d95' # Input your api_hash here

    #creating telegram client
    client = TelegramClient('telegramsession', api_id, api_hash)
    client.start()

    grp = str(input("Where do you wish to scrape members from? (e.g 't.me/name') "))

    initial = int(input("Where do you wish to start? (e.g 23)"))

    async def start():
        
        group = await client.get_entity(grp)
        members = await client.get_participants(group) # Return all users and their information

        channel = await client.get_entity('t.me/orionfinancial')
        
        # t.client.send_message(client.me,"Yooooo")
        

        # await client.send_message("Hutagg", f'{channel.title} Adding New Users')

        n = 0

        for user in members[int(initial)::]:
            if n % 50 == 0 and n != 0:
                print("User Account Has Reach The Max Amount")
                break
            elif user.bot == False:
                try:
                    # users_to_add = await client.get_entity(str(user.username))
                    time.sleep(30)
                    await client(InviteToChannelRequest(
                        channel,
                        [user]
                    ))
                    print(f"Added - {user.id} to {channel}")
                    n += 1

                    # await client.send_message("Hutagg", f"Added {user.username} -- {members.index(user)}")
                    time.sleep(random.randrange(3, 8))                

                except UserPrivacyRestrictedError:
                    time.sleep(3)

                except UserNotMutualContactError:
                    time.sleep(3)

                except UserChannelsTooMuchError:
                    print("There is an error to handle!")
                    time.sleep(1)

                except PeerFloodError:
                    print("Adding was flagged and stopped by Telegram")
                    time.sleep(30)
                    break

                except Exception as e:
                    print(f"Unexpected Error --- {e}")
                    continue

        print("DONE...")


    client.loop.run_until_complete(start())

if __name__ == "__main__":
    main()