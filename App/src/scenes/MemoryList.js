import React, { Component } from 'react';
import {
  Image,
  View,
  Text,
  Alert,
  Dimensions,
  StyleSheet,
  TouchableOpacity
} from 'react-native';
import { Button } from 'native-base';
import { Actions } from 'react-native-router-flux';
import styled from 'styled-components';
import Carousel from 'react-native-snap-carousel';

export default class MemoryList extends Component {
  constructor() {
    super();
    // dummy data
    this.state = {
      playLists: [
        {
          id: '1',
          url: 'https://i.gyazo.com/879874714ef7b1549b4aebab9ba3e470.jpg',
          name: 'SPAJAM2018本戦'
        },
        {
          id: '2',
          url: 'https://i.gyazo.com/879874714ef7b1549b4aebab9ba3e470.jpg',
          name: 'SPAJAM2018本戦'
        },
        {
          id: '3',
          url: 'https://i.gyazo.com/879874714ef7b1549b4aebab9ba3e470.jpg',
          name: 'SPAJAM2018本戦'
        }
      ],
      isOpenModal: false
    }
  }


   renderItem = item => (
     <ItemContainer
       key={item.id}
      >
       <ItemImage source={{uri: 'https://i.gyazo.com/879874714ef7b1549b4aebab9ba3e470.jpg'}} />
       <WhiteText>SPAJAM2018本戦</WhiteText>
     </ItemContainer>
   );

  render(){
    return (
      <Container>
          <View>
            <Carousel
              data={this.state.playLists}
              renderItem={this.renderItem}
              itemWidth={Dimensions.get("window").width * 0.85}
              sliderWidth={Dimensions.get("window").width}
              slideStyle={{ flex: 1 }}
              layout={'stack'}
              loop
              autoPlay
            />
          </View>
      </Container>
    );
  }
}

const Container = styled(View)`
  height: 100%;
  width: 100%;
  background-color: rgb(189, 231, 240);
  position: relative;
`
const ItemContainer = styled(TouchableOpacity)`
  margin: 100px auto;
  margin-left: 40px;
`
const ItemImage = styled(Image)`
  width: 250px;
  height: 350px;
`
const StyledButton = styled(Button)`
  width: 300px;
  margin: 50px auto 0;
  background-color: #F02B60;
`
const BGImage = styled(Image)`
  height: 350;
  width: 350;
  margin-top: 140;
  position: absolute;
  align-self: center;
  z-index: -1;
`
const WhiteText = styled(Text)`
  color: #fff;
  font-size: 18px;
  text-align: center;
  margin: 25px auto 0;
  padding: 15px 30px;
  background-color: #F02B60;
  border-radius: 50px;
`
const LoadingText = styled(Text)`
  color: #fff;
  font-size: 18px;
  text-align: center;
  height: 100%;
  margin-top: 300px;
`