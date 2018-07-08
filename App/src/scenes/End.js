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
  margin: 30px auto 20px;
  width: 280px;
  height: 500px;
`

const StyledButton = styled(Button)`
  margin: 15px 10px;
  backgroundColor: rgb(240, 43, 96);
  border-radius: 10;
`