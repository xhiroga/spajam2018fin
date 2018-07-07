import React, { Component } from 'react';
import { Scene, Router } from 'react-native-router-flux';
import {
  Start,
  Record,
  End
} from './src/scenes'

export default class App extends React.Component {
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