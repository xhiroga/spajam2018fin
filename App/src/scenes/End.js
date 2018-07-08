import React, { Component } from 'react';
import { Image } from 'react-native';
import { Button, Text, View } from 'native-base';
import styled from 'styled-components';
import { Layout } from '../components/';

export default class End extends Component {
  render() {
    return (
      <BackGround>
        <BGImage
          source={require('../../img/bg.png')}
        />
        <MainImage
          source={require('../../img/image.png')}
        />
        <SNSImage
          source={require('../../img/btn5.png')}
        />
        <BackImage
          source={require('../../img/btn6.png')}
        />
        <StyledButton
          full
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

const BackImage = styled(Image)`
  position: absolute;
  top: 445px;
  right: 70px;
  width: 110px;
  height: 40px;
`

const StyledButton = styled(Button)`
  margin: 15px 10px;
  backgroundColor: rgb(240, 43, 96);
  border-radius: 10;
`