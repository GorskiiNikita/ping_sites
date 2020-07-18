import React, {Component} from "react";
import {render} from "react-dom";


class AuthForm extends Component {
    render() {
        return (
            <form className="auth-form" id="auth-form" method="POST"
                  onSubmit={(e) => this.handleSubmit(e)}>
                <label>Логин: <input type="text" name="username" size="25" required id="username"/></label>
                <br />
                <label>Пароль: <input type="password" name="password" size="25" required id="password"/></label>
                <br />
                <button>Войти</button>
            </form>
        )
    }

    clearAuthForm() {
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
    }

    handleSubmit(e) {
        console.log(this.props.s); // без этого не работает
        this.loginUser();
        this.clearAuthForm()
        e.preventDefault();
    }

    loginUser() {
        let formUser = document.getElementById('auth-form');
        let formData = new FormData(formUser);
        fetch('api/login', {
            method: 'POST',
            redirect: 'follow',
            body: formData})
          .then((response) => {
              if (response.redirected) {
                  window.location.href = response.url;
              } else if (response.status === 401) {
                  throw new Error('Failed authenticated');
              }
          })
            .catch(function(err) {
                console.log(err);
            });
    }
}



class App extends Component {
    render() {
        return (
            <AuthForm s={5} /> // без этого не работает
        );
    }
}

const container = document.getElementById("app");
render(<App />, container);