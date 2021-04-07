import time
import random
import scenario


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def print_pause3(message_to_print):
    print(message_to_print)
    time.sleep(3)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("Please select one of the options.")


def select_scenario(towns, monsters):
    template = "'Welcome to {{town}}. The villain, {{monster}}, is nearby.'"
    output = []
    index = 0

    while index < len(template):
        if template[index:index+8] == '{{town}}':
            output.append(random.choice(towns))
            index += 8
        elif template[index:index+11] == '{{monster}}':
            output.append(random.choice(monsters))
            index += 11
        else:
            output.append(template[index])
            index += 1
    output = ''.join(output)
    return output


def arrive():
    print_pause("You are an eager new adventurer!")
    print_pause("You arrive at a bridge leading over a river.")
    print_pause("The guard at the bridge greets you:")
    print_pause("'Hello Traveler!'")
    print_pause3(select_scenario(scenario.towns, scenario.monsters))
    print_pause3("'They have been terrorizing our town for weeks.'")
    print_pause3("'Please help us. This map will guide you.'")
    print_pause3("You look at the map and see the following locations:")
    print_pause3("To the north are the Mountains, to the east a waterfall.")
    print_pause3("To the west lay the plains, and south heads to town.")


def mountain(items):
    print_pause("You head north to the mountains.")
    print_pause3("As you come to the base of the cliffs, you realize you "
                 "can't proceed further without something to help you climb.")
    if "Climbing Gear" in items:
        print_pause("You prepare the climbing gear from the caravan "
                    "and begin to climb.")
        print_pause3("As you ascend onto the peak, you are "
                     "confronted by the villain!")
        print_pause3("They immediately spring into action and charge at you!")
        if "Shield" in items:
            print_pause3("You raise your shield and defend the attack!")
            print_pause3("The villain is stunned by this and "
                         "staggers backwards.")
            if "Sword" in items:
                print_pause3("You take advantage of this opportunity "
                             "and draw your sword.")
                print_pause3("Before the villain is able to regroup, you "
                             "swing and the enemy falls before you.")
                print_pause3("You return to town, victorious. "
                             "The townsfolk thank you.")
                print_pause3("You head off into the sunset, "
                             "towards your next adventure.")
                replay_game()
            else:
                print_pause3("Despite successfully defending the ambush, "
                             "you have no method of counter attack.")
                print_pause3("You must retreat down the mountain before "
                             "you are attacked again.")
                select_path(items)
        else:
            print_pause3("You have no way to defend yourself.")
            print_pause3("You have been defeated.")
            print_pause("Better luck next time!")
            replay_game()
    else:
        print_pause3("Unfortunately, none of your current gear allows "
                     "you to make any further progress.")
        print_pause("You head back away from the mountain.")
        select_path(items)


def waterfall(items):
    print_pause("You head east towards the waterfall.")
    print_pause3("As you arrive, the sun is glistening off the water.")
    if "Shield" in items:
        print_pause3("The cool water refreshes you but there does not seem "
                     "to be anything else useful at this location.")
    else:
        print_pause3("You notice an intense reflection that appears to be "
                     "coming from behind the water.")
        print_pause3("You go to the side and slip around the falls.")
        print_pause3("You find a beautiful and sturdy shield!")
        items.append("Shield")
    print_pause3("You leave the waterfall towards your next destination.")
    select_path(items)


def field(items):
    print_pause("You head west towards the open field.")
    print_pause3("You see a caravan ahead and approach the leader.")
    if "Climbing Gear" in items:
        print_pause3("The caravan leader wishes you luck but has already "
                     "given you a tool that will aid your quest")
    else:
        print_pause("You tell him about your quest to help the nearby town.")
        print_pause3("They have been unable to trade with the town due to "
                     "the constant attacks.")
        print_pause3("He agrees to give you some climbing "
                     "gear that will allow you to climb the nearby mountain.")
        items.append("Climbing Gear")
    print_pause3("You leave the field towards your next destination.")
    select_path(items)


def town(items):
    print_pause("You head south towards town.")
    print_pause3("Upon entering, you ask to see the blacksmith.")
    if "Sword" in items:
        print_pause("The blacksmith asks how your adventure is going.")
        print_pause3("She wishes there was more she could do but there "
                     "is nothing else helpful in town.")
    else:
        print_pause("The blacksmith is excited to see an adventurer.")
        print_pause3("She eagerly gifts you with her best sword!")
        items.append("Sword")
    print_pause3("You leave town towards your next destination.")
    select_path(items)


def select_path(items):
    response = valid_input("Please enter the path you would like to take:\n"
                           "N. Mountain\n"
                           "E. Waterfall\n"
                           "W. Field\n"
                           "S. Town\n"
                           "Select 'North', 'East', 'West', or 'South'\n",
                           ["north", "east", "west", "south"])
    if "north" in response:
        mountain(items)
    elif "east" in response:
        waterfall(items)
    elif "west" in response:
        field(items)
    elif "south" in response:
        town(items)


def replay_game():
    response = valid_input("Would you like to play again?\n"
                           "Please select 'yes' or 'no':\n",
                           ["yes", "no"])
    if "no" in response:
        print_pause("Thank you for playing!")
    elif "yes" in response:
        print_pause("Get Ready to Play Again!")
        play_game()


def play_game():
    items = []
    arrive()
    select_path(items)


if __name__ == '__main__':
    play_game()
