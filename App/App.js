import React, { Component } from 'react';
import { Scene, Router } from 'react-native-router-flux';
import * as firebase from 'firebase';
import styled from 'styled-components';
import { firebaseConfig } from './utils';
import {
  Top,
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
      <StyledRouter>
        <Scene key="root">
          <Scene key="top" component={Top} title="Top" initial/>
          <Scene key="start" component={Start} title="Start" />
          <Scene key="record" component={Record} title="Record" />
          <Scene key="end" component={End} title="End" />
        </Scene>
      </StyledRouter>
    );
  }
}

const StyledRouter = styled(Router)`
  backgroundColor: rgb(189, 231, 240);
`