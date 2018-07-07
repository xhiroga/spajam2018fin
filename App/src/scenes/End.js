import React, { Component } from 'react';
import { Button, Text } from 'native-base';
import styled from 'styled-components';
import { Layout } from '../components/';

export default class End extends Component {
  render() {
    return (
      <Layout>
        <StyledButton
          full
        >
          <Text>Start</Text>
        </StyledButton>
      </Layout>
    )
  }
}

const StyledButton = styled(Button)`
  margin: 15px 10px;
`