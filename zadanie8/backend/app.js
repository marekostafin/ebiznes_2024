const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const cors = require('cors');
const createError = require('http-errors');
const express = require('express');
const logger = require('morgan');
const path = require('path');
const session = require('express-session');

const app = express();
app.use(cors());

app.use(session({
  secret: 'your_secret_key',
  resave: false,
  saveUninitialized: true,
  cookie: { secure: false }
}));

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

const users = [
  {username: 'useruser', password: 'qwerty' },
  {username: 'admin', password: 'admin' },
];

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = users.find(findUser => findUser.username === username && findUser.password === password);
  if (user) {
    req.session.user = username;
    res.json({ message: 'Login successful', user: user });
  } else {
    res.status(401).send({ message: 'Invalid username or password'});
  }
});

app.post('/logout', (req, res) => {
  req.session.destroy(err => {
    if (err) {
      return res.json({ message: 'Error encountered while logging out' });
    }
    res.json({ message: 'Logout successful' });
  });
});

app.post('/register', (req, res) => {
  const { username, password } = req.body;
  if (users.find(findUser => findUser.username === username)) {
    return res.json({ message: 'Username already exists' });
  }

  const newUser = { username, password };
  users.push(newUser);
  res.json({ message: 'Registration successful', user: newUser });
});

app.post('/verify', (req, res) => {
  if(req.session.user) {
    return res.status(200).json({ message: 'User verified successfully' });
  } else {
    return res.status(401).json({ message: 'User not authorized' });
  }
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
