# Discord webhook plugin

This plugin calls remote API.

# Configuration

```json
{
  "url": "https://discord.com/api/webhooks/879132030/kXYSPpId..."
}
```

This configuration requires discord webhook url.

# Payload

Payload for this plugin defines a message to be sent. 

Example:

```json
{
  "message": "this is test message",
  "username": "user name"
}
```

# Result

This plugin returns either the response (on response port) or and error on error port.

Valid response is:

```json
{
  "status": 204
}
```
