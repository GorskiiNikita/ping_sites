import React, { Component } from "react";
import SiteItem from "./SiteItem";
import AddSiteForm from "./AddSiteForm";


function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}


class ListSites extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
        };
    }

    componentDidMount() {
        this.updateData();
        this.timerID = setInterval(
            () => this.updateData(),
            5000
        );
    }

    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    render() {
        return (
            <div>
                <ul>
                  {this.state.data.map((item, index) => {
                      return <SiteItem siteItem={item}
                                       key={item.id}
                                       onDelete={() => this.handleClickDeleteItem(item.id, index)}
                                       onUpdate={() => this.handleClickUpdateItem(item.id, index)}/>;
                  })}
              </ul>
                <AddSiteForm onAdd={() => this.handleClickAddSite()}/>
            </div>
        );
    }

    updateData() {
        fetch('api/check-list')
            .then(response => response.json())
            .then(data => {
                this.setState(() => {return {data: data.data};});
            });
    }

    handleClickDeleteItem(i, key) {
        fetch('api/check-list/' + i, {
            method: 'DELETE',
            headers: {'Access-Control-Allow-Methods': 'DELETE', 'X-CSRFTOKEN': getCookie('csrftoken')},
            credentials: 'include'})
          .then(() => {
                this.setState(() => {
                    return {data: this.state.data.slice(0, key).concat(this.state.data.slice(key + 1))};
                });
            });
    }

    handleClickUpdateItem(i, key) {
        let formSite = document.getElementById('siteForm' + i);
        let formData = new FormData(formSite);
        formData.set('notification', String((formData.get('notification') === 'on')));
        fetch('api/check-list/' + i + '/', {
            method: 'PATCH',
            body: formData,
            headers: {'Access-Control-Allow-Methods': 'PUT', 'X-CSRFTOKEN': getCookie('csrftoken')},
            credentials: 'include'})
          .then((response) => response.json())
            .then((siteItem) => {
                let data = this.state.data.slice();
                data[key] = siteItem;
                this.setState(() => {
                    return {data: data};
                });
            });
    }

    handleClickAddSite() {
        let formSite = document.getElementById('adding-form');
        let formData = new FormData(formSite);
        formData.set('notification', String((formData.get('notification') === 'on')));
        fetch('api/check-list/', {
            method: 'POST',
            body: formData,
            headers: {'Access-Control-Allow-Methods': 'PUT', 'X-CSRFTOKEN': getCookie('csrftoken')},
            credentials: 'include'})
          .then((response) => response.json())
            .then((siteItem) => {
                let data = this.state.data.slice();
                data.push(siteItem);
                this.setState(() => {
                    return {data: data};
                });
            });
    }
}


export default ListSites;
