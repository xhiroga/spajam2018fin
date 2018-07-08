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
        <Scene key="root" navigationBarStyle={{ backgroundColor: '#59CADE'}} >
          <Scene key="top" component={Top} title="ホーム" titleStyle={{ color: '#fff'}} initial/>
          <Scene key="start" component={Start} titleStyle={{ color: '#fff'}} headerBackTitleStyle={{ color: '#fff' }} title="タグをつける" />
          <Scene key="record" component={Record} titleStyle={{ color: '#fff'}} headerBackTitleStyle={{ color: '#fff' }} title="ログをとる" />
          <Scene key="end" component={End} titleStyle={{ color: '#fff'}} headerBackTitleStyle={{ color: '#fff' }} title="完成" />
        </Scene>
      </StyledRouter>
    );
  }
}

const StyledRouter = styled(Router)`
  backgroundColor: rgb(189, 231, 240);
`