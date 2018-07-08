import React, { Component } from 'react';
import { Actions } from 'react-native-router-flux';
import { Constants, Location, Permissions } from 'expo';
import { Button, Text } from 'native-base';
import styled from 'styled-components';
import { Layout } from '../components/';
import { Platform } from 'react-native';
import { w3wClient } from "../../utils/apiClient";
import * as firebase from 'firebase';
import moment from 'moment';

export default class Record extends Component {
  constructor() {
    super();
    this.state = {
      location: null,
      locationErrorMessage: null
    };
  }

  componentWillMount() {
    if (Platform.OS === 'android' && !Constants.isDevice) {
      this.setState({
        locationErrorMessage: 'Oops, this will not work on Sketch in an Android emulator. Try it on your device!',
      });
    } else {
      this.setState({
        intervalId: setInterval(this.getLocationAsync, 3000)
      });
    }
  }

  // GPS情報を取得
  getLocationAsync = async () => {
    let { status } = await Permissions.askAsync(Permissions.LOCATION);
    if (status !== 'granted') {
      this.setState({
        locationErrorMessage: 'Permission to access location was denied',
      });
    }

    let location = await Location.getCurrentPositionAsync({});

    this.writeLocationToFirebase(location);
    this.setState({ location });
  };

  writeLocationToFirebase(location) {
    firebase.database().ref("coodinates/" + moment().format()).set({
      latitude: location.coords.latitude,
      longitude: location.coords.longitude
    });
  }

  onPressButton() {
    clearInterval(this.state.intervalId);
    this.setState({
      intervalId: null
    });
    Actions.end();
  }

  render() {
    let text = 'Waiting..';
    if (this.state.locationErrorMessage) {
      text = this.state.locationErrorMessage;
    } else if (this.state.location) {
      text = JSON.stringify(this.state.location);
    }

    return (
      <Layout>
        <StyledButton
          full
          onPress={() => this.onPressButton()}
        >
          <Text>{text}</Text>
          <Text>End</Text>
        </StyledButton>
      </Layout>
    )
  }
}

const StyledButton = styled(Button)`
  margin: 15px 10px;
`