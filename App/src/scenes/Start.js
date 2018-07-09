import React, { Component } from 'react';
import { Actions } from 'react-native-router-flux';
import * as firebase from 'firebase';
import { Image } from 'react-native';
import { FIREBASE_DATABASE_URL } from 'react-native-dotenv'
import { View, Content, Input, Button, Text } from 'native-base';
import styled from 'styled-components';
import { Layout } from '../components/';

export default class Start extends Component {
  constructor(props){
    super(props);
    this.state = {
      hashtag: ''
    };
  }

  submitText = async(text) => {
    // オブジェクト型でハッシュタグを保存し保存先のURLを取得
    const hashtagUrl = await firebase.database().ref("/hashtags").push(text);
    const hashtagId = await this.getHashtagId(hashtagUrl)
    Actions.record({ hashtagId }); // 記録画面へidを渡す
  }

  getHashtagId = hashtagUrl => {
    const url = FIREBASE_DATABASE_URL + "/hashtags/"
    return hashtagUrl.toString().replace(url, '');
  }

  render() {
    const { hashtag } = this.state;
    return (
      <BackGround>
      <Layout>
        <Content>
          <StyledImage
            source={require('../../img/tag.png')}
          />
          <Tag>
            <StyledInput
              value={hashtag}
              onChangeText={(text) => this.setState({hashtag: text})}
            />
          </Tag>
          <StyledButton
            full
            onPress={() => this.submitText(hashtag)}
          >
            <Text>このタグで出発</Text>
          </StyledButton>
        </Content>
      </Layout>
    </BackGround>
    )
  }
}

const BackGround = styled(View)`
  backgroundColor: rgb(189, 231, 240);
  flex: 1;
`
const StyledButton = styled(Button)`
  margin: 250px 10px 15px;
  background-color: #F02B60;
  border-radius: 5;
`
const StyledImage = styled(Image)`
  width: 292px;
  height: 143px;
  top: 150px;
  right: 10%;
  bottom: 0px;
  left: 10%;
  margin: 0 auto;
  position: absolute;
  z-index: -1;
`
const Tag = styled(View)`
  width: 100%;
  margin: 120px auto 0px;
`
const StyledInput = styled(Input)`
  z-index: 3;
  width: 50%;
  margin: 100px auto 0px;
  font-size: 24px;
`