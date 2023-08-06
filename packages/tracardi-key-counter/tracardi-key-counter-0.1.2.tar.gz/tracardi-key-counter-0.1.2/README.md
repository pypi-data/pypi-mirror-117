# Key counter plugin

This plugin counts keys provided in payload.

# Configuration

```json
{
  "path": "profile@stats.counters.MobileVisits"
}
```

This configuration indicated that profile has some stats at stats.counters.MobileVisits 
that count keys in form of a dict:

```json
{
  "key1": 1,
  "key2": 33,
  ...
}
```

This is the place where additional counts will be saved.

# Payload

Payload for this plugin must be either string or list of stings. Each string is a key to be counted.

For example if you count mobile and desktop visits. Get the agent type from context sent in event. 
And cut out information on platform and send it to this plugin to be counted. One this it will be 'mobile',
other time it will be 'desktop' depending on the platform the customer is using. 

Example of payload:

```json
{
  "payload": "mobile"
}
```

or if multiple key as being sent. 

```json
{
  "payload": ["mobile", "android"]
}
```
