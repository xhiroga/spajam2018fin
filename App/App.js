import React, { Component } from 'react';
import { Scene, Router } from 'react-native-router-flux';
import * as firebase from 'firebase';
import { firebaseConfig } from './utils';
import {
  Start,
  Record,
  End
} from './src/scenes'

export default class App extends Component {
  componentWillMount() {
    firebase.initializeApp(firebaseConfig);
  }
  render() {
    return (
      <Router>
        <Scene key="root">
          <Scene key="start" component={Start} title="Start" initial/>
          <Scene key="record" component={Record} title="Record" />
          <Scene key="end" component={End} title="End" />
        </Scene>
      </Router>
    );
  }
}