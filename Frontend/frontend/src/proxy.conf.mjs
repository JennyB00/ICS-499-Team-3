export default [
  {
    context: [
        '/accounts',
        '/chats',
        '/contacts',
        '/past_chats',
        '/messages',
        '/privileges',
        '/bot'
    ],
    target: 'http://localhost:8000',
    secure: false
  }
];
