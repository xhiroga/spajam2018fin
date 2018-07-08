import React, { Component } from 'react';
import { Actions } from 'react-native-router-flux';
import * as firebase from 'firebase';
import { Content, Input, Item, Button, Text } from 'native-base';
import styled from 'styled-components';
import { Layout } from '../components/';

export default class Start extends Component {
  constructor(props){
    super(props);
    this.state = {
      hashtag: ''
    };
  }

  submitText = () => {
    firebase.database().ref("/hashtags").set({text: this.state.hashtag});
    Actions.record();
  }

  render() {
    const { hashtag } = this.state;
    return (
      <Layout>
        <Content>
          <Text>旅にタグはつきものです</Text>
          <Item regular>
            <Input
              value={hashtag}
              placeholder='Regular Textbox'
              onChangeText={(text) => this.setState({hashtag: text})}
            />
          </Item>
          <StyledButton
            full
            onPress={() => this.submitText()}
          >
            <Text>Start</Text>
          </StyledButton>
        </Content>
      </Layout>
    )
  }
}

const StyledButton = styled(Button)`
  margin: 15px 10px;
`