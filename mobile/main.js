import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  Button,
  Linking,
  Alertk,
  Modal,
  WebView,
  TextInput
} from 'react-native';

import config from './config';

export default class Main extends Component {
  constructor(props) {
    super(props);

    this.handlePress = this.handlePress.bind(this);

    this.state = {
      showModal: false
    }
  }

  handlePress() {
    this.setState({showModal: true});
  }

  render() {
    const {transport, appId, permissions, endpoint} = config;

    const uri = `${endpoint}authenticate/${appId}?permissions=${permissions}&transport=${transport}`;

    return (
      <View style={styles.container}>
        <Text style={styles.welcome}>
          Authenticate with Bitwala
        </Text>
        <Button onPress={this.handlePress} title="Authenticate"/>
        <TextInput
          style={{
            marginTop: 10,
            height: 40,
            borderWidth: 1,
            borderColor: 'gray',
            marginHorizontal: 10,
            paddingHorizontal: 10
          }}
          placeholder="Enter your Bitwala token..."
        />
        <Modal animationType={"slide"} transparent={false} visible={this.state.showModal} onRequestClose={() => {this.setState({showModal: false})}}>
          {this.state.showModal
            && <WebView source={{uri}} />
          }
          <Button onPress={() => {this.setState({showModal: false})}} title="Close"/>
        </Modal>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
});
