import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  Button,
  Linking,
  Alertk
} from 'react-native';

export default class Main extends Component {

  handlePress() {
    const transport = 'COPY';

    // Building the URL
    const appId = 'TDSjjoxb2bMAvGhQ2';
    const permissions = 'bank_transfers_manage';

    const url = `http://sandbox.bitwala.io/authenticate/${appId}?permissions=${permissions}&transport=${transport}`;

    Linking.openURL(url)
      .catch(err => Alert.alert('Couldn\'t open link'));
  }

  render() {

    return (
      <View style={styles.container}>
        <Text style={styles.welcome}>
          Authenticate with Bitwala
        </Text>
        <Button onPress={this.handlePress} title="Authenticate"/>
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
