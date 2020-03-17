#!/usr/bin/python

'''
params:
    - text     <multiline: ok> # not really yet
    - color    <default: black>
    - bgColor  <default: None>
    - fontSize <default: 1.2em>
    - fontFace <default: monospace>
    - radius   <default: 5>

returns:
    svg document
'''
def toSvg(
        text='',
        color='black',
        bgColor=None,
        fontSize="1.2em",
        font='monospace',
        radius=3,
    ):

    width = 0.6 * len(text)

    background = f'<rect fill="{bgColor}" width="100%" height="100%" rx="{radius}"/>' if bgColor is not None else ''

    return f"""<?xml version="1.0" encoding="utf-8"?>
        <svg version="1.1"
             xmlns="http://www.w3.org/2000/svg"
             xmlns:xlink="http://www.w3.org/1999/xlink"
             width="{width}em" height="1em"
        >
          {background}
          <text font-size="{fontSize}" font-family="{font}" x=".1em" y="1em">
            <tspan fill="{color}">{text}</tspan>
          </text>
        </svg>"""

def lambda_handler(event, context):
    svg = toSvg(**event['queryStringParameters'])
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'image/svg+xml',
        },
        'body': svg,
    }
