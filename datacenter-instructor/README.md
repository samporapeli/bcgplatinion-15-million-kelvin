First, create a `config.js` file with contents like this:
```js
module.exports = {
  authKey: 'your-auth-key-here',
  preferredDC: 'FR', // initial preferred location
  workCommand: 'sleep 0.5',
}
```

Then
```bash
npm install
# production
npm run start
# dev
npm run dev
```
