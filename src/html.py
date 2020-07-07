def info():
    return '''<html>
    <body>
      <h1>Help!</h1>
      <p>Commands can be sent with GET Or POST request to '*/send_movement_command/{direction}</p>
      <p>List of supported {direction} strings:</p>
      <ul>
        <li>forward</li>
        <li>backward</li>
        <li>stop</li>
        <li>left</li>
        <li>right</li>
      </ul>
    </body>
    </html>'''

def failure(message='Unknown error'):
    return '''
    <html>
       <body>
          <h1>Movement Failed</h1>
          <p>{}</p>
       </body>
    </html>
    '''.format(message)

def success(message='No obvious errors'):
    return '''
    <html>
       <body>
          <h1>Movement Successful</h1>
          <p>{}</p>
       </body>
    </html>
    '''.format(message)
