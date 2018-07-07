import React, { Component } from 'react';
import { Actions } from 'react-native-router-flux';
import { Button, Text } from 'native-base';
import styled from 'styled-components';
import { Layout } from '../components/';

export default class Record extends Component {
  render() {
    return (
      <Layout>
        <StyledButton
          full
          onPress={() => Actions.record()}
        >
          <Text>End</Text>
        </StyledButton>
      </Layout>
    )
  }
}

const StyledButton = styled(Button)`
  margin: 15px 10px;
`