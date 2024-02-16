import mido
from mido import Message, MidiFile, MidiTrack, get_input_names

def main():
    # List all available MIDI input ports
    print("Available MIDI inputs:", get_input_names())

    # User choose from list
    port_name = input("Enter the name of your MIDI input: ")

    # Open the port
    with mido.open_input(port_name) as inport:
        print("Listening for MIDI messages on '{}'...".format(port_name))
        
        for msg in inport:
            if msg.type == 'note_on' or msg.type == 'note_off':
                print(msg)

if __name__ == "__main__":
    main()
