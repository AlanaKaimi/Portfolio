import React, { Component } from "react";

import axios from "axios";

export default class Art extends Component {
  constructor(props) {
    super(props);
    this.state = {
    arts:[],
    };
    this.loadArts = this.loadArts.bind(this);
  }

  componentWillMount() {
    this.loadArts();
  }

  async loadArts()
  {
    const promise = await axios.get("http://localhost:3000/art");
    const status = promise.status;
    if(status===200)
    {
      const data = promise.data.data;
      this.setState({arts:data});
    }
  }

  render() {
    return(
      <div>
        <h1>Art</h1>
            {this.state.arts.map((value,index)=>{return <h4 key={index}>{value}</h4>})}
      </div>
    )
  }
}