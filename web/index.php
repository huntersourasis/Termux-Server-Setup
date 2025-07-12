<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Termux PHP Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {
            --bg-color: #121212;
            --card-color: #1e1e1e;
            --accent-color: #4CAF50;
            --text-color: #e0e0e0;
            --muted-text: #a0a0a0;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .container {
            background-color: var(--card-color);
            border-radius: 12px;
            padding: 40px;
            max-width: 600px;
            text-align: center;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }

        h1 {
            color: var(--accent-color);
            font-size: 2.5em;
            margin-bottom: 20px;
        }

        p {
            color: var(--muted-text);
            font-size: 1.1em;
            line-height: 1.6em;
        }

        code {
            background-color: #2a2a2a;
            padding: 3px 6px;
            border-radius: 5px;
            color: #f8f8f2;
            font-family: 'Courier New', Courier, monospace;
        }

        footer {
            margin-top: 30px;
            font-size: 0.9em;
            color: #666;
        }

        @media (max-width: 600px) {
            .container {
                margin: 20px;
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Termux Web Server</h1>
        <p>Your local PHP server is <strong>up and running</strong>.</p>
        <p>Place your website files in the <code>~/termux-server/</code> directory.</p>
        <p>You can access your server at:</p>
        <p><code>http://<?php echo getHostByName(getHostName()); ?>:8090</code> or your device's local IP</p>
        <footer>Managed by <strong>Termux PHP Web Server Setup Tool</strong></footer>
    </div>
</body>
</html>
