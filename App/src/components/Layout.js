import React from 'react';
import { Container, Content } from 'native-base';

const Layout = ({ children }) => (
  <Container>
    <Content>
      {children}
    </Content>
  </Container>
);

export default Layout;