import React, { Component } from 'react';
import { Actions } from 'react-native-router-flux';
import { Constants, Location, Permissions } from 'expo';
import { View, Button, Text } from 'native-base';
import styled from 'styled-components';
import { Layout } from '../components/';
import { Platform, Image, Alert } from 'react-native';
import { w3wClient, sawaraClient } from "../../utils/apiClient";
import * as firebase from 'firebase';
import moment from 'moment';

export default class Record extends Component {
  constructor() {
    super();
    this.state = {
      location: null,
      locationErrorMessage: null,
      buttonName: "一時停止",
      status: false
    };
  }

  componentWillMount() {
    if (Platform.OS === 'android' && !Constants.isDevice) {
      this.setState({
        locationErrorMessage: 'Oops, this will not work on Sketch in an Android emulator. Try it on your device!',
      });
    } else {
      // 3分ごとに位置情報をfirebaseへ送る
      this.setState({
        intervalId: setInterval(this.getLocationAsync, 180000),
        status: true
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
    firebase.database()
      .ref("/hashtags/" + this.props.hashtagId + "/coordinates")
      .push({
        latitude: location.coords.latitude,
        longitude: location.coords.longitude,
        timestamp: moment().format()
      });
  }

  onPressButton() {
    const { hashtagId } = this.props;
    clearInterval(this.state.intervalId);
    this.setState({
      intervalId: null,
      status: false
    });

    // sawaraAPIができ次第コメントを外す

    sawaraClient.get("/")
      .then(
        res => {
          console.log(res.data);
          Actions.end({ hashtagId });
        })
      .catch(
        err => {
          console.log(err.request);
          Actions.end({ hashtagId });
          // Alert.alert(
          //   'APIを叩く際にエラーが発生しました。',
          //   '',
          //   [
          //     {text: 'OK', onPress: () => console.log('on press alert button')},
          //   ],
          //   { cancelable: false }
          // )
        });
    // Actions.end();
  }

  onPressCancelButton() {
    if (this.state.intervalId == null) {
      // 3分ごとに位置情報をfirebaseへ送る
      this.setState({
        intervalId: setInterval(this.getLocationAsync, 180000),
        buttonName: '一時停止',
        status: true
      });
    } else {
      clearInterval(this.state.intervalId);
      this.setState({
        intervalId: null,
        buttonName: '再開',
        status: false
      });
    }
  }

  render() {

    return (
      <BackGround>
        {
          this.state.status
          ? (<CycleImage
              source={require('../../img/circle.png')}
            />)
          : (<CycleImage
              source={require('../../img/circle2.png')}
            />)
        }
        <StopButton
          full
          onPress={() => this.onPressCancelButton()}
        >
          <Text>{this.state.buttonName}</Text>
        </StopButton>
        <FinishButton
          full
          onPress={() => this.onPressButton()}
        >
          <Text>旅の記録を終了</Text>
        </FinishButton>
      </BackGround>
    )
  }
}

const BackGround = styled(View)`
  backgroundColor: rgb(189, 231, 240);
  flex: 1;
`

const CycleImage = styled(Image)`
  width: 300px;
  height: 309px;
  margin: 10px auto;
  marginTop: 50px;
`

const StopButton = styled(Button)`
  margin: 80px 10px 10px;
  background-color: #B1B1B1;
  border-radius: 5;
`

const FinishButton = styled(Button)`
  margin: 10px;
  border-radius: 5;
  background-color: #F02B60;
`
