locations = {
    'Front Gate': {
        'description': "The iron gates stand half-open, their rusted bars twisted beneath years of neglect. Beyond them, a cracked gravel path winds through overgrown grounds towards the looming silhouette of the asylum. The stone pillars on either side bear the scars of weather and vandalism, their faded lettering barely legible beneath patches of moss. A cold wind carries the smell of damp earth and rotting leaves, while somewhere beyond the walls, a distant metallic clanging echoes through the stillness. The gate hangs strangely silent, as though the world beyond has been holding its breath.",
        'visited': False,
        'paths': {
            '1':{
                'description': 'Push on to the Asylum',
                'destination': 'Courtyard'
            },
        }

    },
    'Courtyard': {
        'description':'The gravel path winds between patches of dead grass and overgrown flowerbeds, leading towards the imposing façade of the asylum. Weathered stone statues stand among the weeds, their faces worn smooth by years of rain. Tall, narrow windows stare down from the upper floors, most dark and lifeless, though you cannot shake the feeling that something watches from behind the glass. The closer you approach, the quieter the world becomes, until even the wind seems to die against the towering walls. At the end of the path, a short flight of stone steps rises to a pair of enormous wooden doors, their iron fittings blackened with age. Deep scratches mar the wood around the handles, and something dark has seeped into the cracks between the planks. You climb the steps and stop before the entrance. The doors stand silently before you, their weathered surface concealing whatever waits within.',
        'visited': False,
        'paths': {
            '1': {
                'description':'Open the doors and enter... The Asylum',
                'destination':'Entrance Hall'

            },
        }
    },
    'Entrance Hall': {
        'description':'The heavy doors open onto a dust-covered hall. Ahead, the grand staircase has completely collapsed, leaving a jumble of stone and splintered timber blocking access to the upper floors. To one side, a locked and bared rusted iron gate seal a corridor marked *Patient Ward*, the faded sign barely legible above the grime.Opposite, a broad counter reinforced with iron bars separates the hall from a larger reception area. Beyond it, filing cabinets and scattered desks fill the gloom, with two doors set into the far wall, one hanging ajar and the other firmly shut. With the staircase impassable, and the way to the wards locked, reception offers the only obvious route deeper into the asylum.',
        'visited': False,
        'paths': {
            '1': {
                'description':'Head through to reception',
                'destination':'Reception'
           
            },
            'locked_door': {
                'description': 'attempt to open ward',
                'destination': 'Patient Ward',
                'key': 'Ward Key',
                'unlocked': False
            },

        }
    },
    'Reception': {
        'description':"The reception area is cluttered with overturned chairs, dusty desks and scattered patient records. Pigeonholes line the wall behind the counter, their contents yellowed with age. Two doors stand opposite, leading to separate rooms. A faded sign identifies one as the Archives, while the other bears a tarnished nameplate marked Administrator's Office. The door to the archives hangs ajar, while the administrator's office remains firmly shut. A narrow doorway at the side of the counter leads back into the entrance hall.",
        'visited': False,
        'paths': {
            '1': {
                'description':'Open the door to the Administrators Office',
                'destination':'Administrators Office'

            },
            '2': {
                'description':'Enter the Archives',
                'destination':'Archives'
            },
        }
    },
    'Administrators Office': {
        'description':"place holder",
        'visited': False
    },
    'Archives': {
        'description':"place holder",
        'visited': False
    },
    'Patient Ward': {
        'description':"place holder",
        'visited': False,
        'paths': {
            '1': {
                'description':'Head toward the cells',
                'destination':'Cells'

            },
            '2': {
                'description':'Enter the Chapel',
                'destination':'Chapel'
            },
            '3': {
                'description':'place holder',
                'destination':'Basement History'
            },
        }
    }    
}

