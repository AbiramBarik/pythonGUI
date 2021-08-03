import PySimpleGUI as sg
from random import randint
window, previous_total, dice, total = None, -1, [], 0
while True:         #Main Dice Rolling Loop
    layout = [[sg.Column([dice])], [sg.Text('Number of Dice:')],[sg.In(size=(3,1), key='_NUM_DICE_')],[sg.Button('Roll Dice', bind_return_key=True)],
                [sg.Text('Total:', font='ANY 20', text_color='red')],
                [sg.Text('   ',size=(3,1), key='_TOTAL_', font='ANY 20', text_color = 'red')],]
    if previous_total != total:
        window.Close() if window is not None else None
        window = sg.Window('Dice Roller', layout).Finalize()
    window.Element('_TOTAL_').Update(total)
    while True:                             # Loop to read # dice to roll, create list of images
        event, values = window.Read()
        if event is None:
            exit()
        try:
            num_dice = int(values['_NUM_DICE_'])
        except:
            continue
        if 8 < num_dice < 0:
            continue
        previouis_dice = dice
        dice, total = [], 0
        for i in range(num_dice):           # for each die rolled, get the random # and build list of images
            die = randint(1,6)
            dice += [sg.Image(filename=r'images/index_{}.png'.format(die), size=(250,250))]
            total += die
        break