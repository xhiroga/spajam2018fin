import React, { Component } from 'react';
import { Image, CameraRoll, Alert } from 'react-native';
import { Button, Text, View } from 'native-base';
import styled from 'styled-components';
import { Actions } from 'react-native-router-flux';
import { Layout } from '../components/';

const image = '../../img/image.png';

export default class End extends Component {

  // 画像の保存
  onPressSave() {
    Promise
      .resolve()
      .then(() => {
        CameraRoll.saveToCameraRoll(image);
      })
      .then(() => {
        Alert.alert(
          '画像を保存しました',
          'My Alert Msg',
          [
            {text: 'OK', onPress: () => console.log('press Ok')},
          ],
          { cancelable: false }
          )
      });
  }

  render() {
    return (
      <BackGround>
        <BGImage
          source={require('../../img/bg.png')}
        />
        <MainImage
          source={require(image)}
        />
        <SNSImage
          source={require('../../img/btn5.png')}
        />
        <BackButton
          title={' '}
          onPress={() => this.onPressSave()}
        >
          <BackImage
            source={require('../../img/btn6.png')}
          />
        </BackButton>
        <StyledButton
          full
          onPress={() => Actions.popTo('top')}
        >
          <Text>ホームに戻る</Text>
        </StyledButton>
      </BackGround>
    )
  }
}

const BackGround = styled(View)`
  backgroundColor: rgb(189, 231, 240);
  flex: 1;
`

const BGImage = styled(Image)`
  margin: 20px auto 10px;
  width: 270px;
  height: 495px;
  position: relative;
`

const MainImage = styled(Image)`
  position: absolute;
  width: 210px;
  height: 305px;
  left: 82px;
  top: 125px;
`

const SNSImage = styled(Image)`
  position: absolute;
  top: 445px;
  left: 70px;
  width: 110px;
  height: 40px;
`

const BackButton = styled(Button)`
  position: absolute;
  top: 445px;
  right: 70px;
  opacity: 1;
  height: 39px;
`

const BackImage = styled(Image)`
  height: 40px;
  width: 110px;
`

const StyledButton = styled(Button)`
  margin: 15px 10px;
  backgroundColor: rgb(240, 43, 96);
  border-radius: 10;
`