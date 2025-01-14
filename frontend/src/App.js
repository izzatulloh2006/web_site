import React from "react";
import axios from "axios";
import "./App.css";
import "./index"
// import "./Izzatulloh.png"
import IzzatullohLogo from './Izzatulloh.png';


class App extends React.Component {
  state = {
    isAuthenticated: false,
    phone_number: "",
    password: "",
    confirm_password: "",
    first_name: "",
    last_name: "",
    login_phone_number: "",
    login_password: "",
  };

  handleChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = async (e) => {
    e.preventDefault();
    const { phone_number, password, confirm_password, first_name, last_name } = this.state;

    if (password !== confirm_password) {
      alert("Passwords do not match");
      return;
    }

    const requestData = { phone_number, password, confirm_password, first_name, last_name };

    try {
      await axios.post("http://127.0.0.1:8000/api/v1/users/", requestData, {
        headers: { "Content-Type": "application/json" },
      });
      alert("Registration successful!");
    } catch (error) {
      console.error(
        "Registration error:",
        error.response ? error.response.data : error.message
      );
    }
  };

  handleLoginSubmit = async (e) => {
    e.preventDefault();
    const { login_phone_number, login_password } = this.state;

    const loginData = { phone_number: login_phone_number, password: login_password };

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/v1/token/", loginData, {
        headers: { "Content-Type": "application/json" },
      });
      alert("Login successful!");
      this.setState({ isAuthenticated: true });
    } catch (error) {
      console.error("Login error:", error.response ? error.response.data : error.message);
    }
  };

  render() {
    const { isAuthenticated } = this.state;

    return (
      <div className="container">
        {isAuthenticated ? (
          <HomePage />
        ) : (
          <div className="forms">
            <div className="form-container">
              <LoginForm
                handleLoginSubmit={this.handleLoginSubmit}
                handleChange={this.handleChange}
                login_phone_number={this.state.login_phone_number}
                login_password={this.state.login_password}
              />
            </div>
            <div className="form-container">
              <RegisterForm
                handleSubmit={this.handleSubmit}
                handleChange={this.handleChange}
                phone_number={this.state.phone_number}
                password={this.state.password}
                confirm_password={this.state.confirm_password}
                first_name={this.state.first_name}
                last_name={this.state.last_name}
              />
            </div>
          </div>
        )}
      </div>
    );
  }
}

const LoginForm = ({ handleLoginSubmit, handleChange, login_phone_number, login_password }) => (
  <form onSubmit={handleLoginSubmit}>
    <h2>Login</h2>
    <label htmlFor="login_phone_number">Phone Number</label>
    <input
      type="text"
      id="login_phone_number"
      name="login_phone_number"
      required
      onChange={handleChange}
      value={login_phone_number}
    />

    <label htmlFor="login_password">Password</label>
    <input
      type="password"
      id="login_password"
      name="login_password"
      required
      onChange={handleChange}
      value={login_password}
    />

    <input type="submit" value="Login" />
  </form>
);

const RegisterForm = ({ handleSubmit, handleChange, phone_number, password, confirm_password, first_name, last_name }) => (
  <form onSubmit={handleSubmit}>
    <h2>Register</h2>
    <label htmlFor="phone_number">Phone Number</label>
    <input
      type="text"
      id="phone_number"
      name="phone_number"
      required
      onChange={handleChange}
      value={phone_number}
    />

    <label htmlFor="password">Password</label>
    <input
      type="password"
      id="password"
      name="password"
      required
      onChange={handleChange}
      value={password}
    />

    <label htmlFor="confirm_password">Confirm Password</label>
    <input
      type="password"
      id="confirm_password"
      name="confirm_password"
      required
      onChange={handleChange}
      value={confirm_password}
    />

    <label htmlFor="first_name">First Name</label>
    <input
      type="text"
      id="first_name"
      name="first_name"
      required
      onChange={handleChange}
      value={first_name}
    />

    <label htmlFor="last_name">Last Name</label>
    <input
      type="text"
      id="last_name"
      name="last_name"
      required
      onChange={handleChange}
      value={last_name}
    />

    <input type="submit" value="Register" />
  </form>
);

const HomePage = () => (
  <div>
    <header>
      <div className="logo">
        <img src={IzzatullohLogo} alt="Izzatulloh Logo" />
        <h1>Izzatulloh Blog</h1>
      </div>
      <nav className="nav">
        <a href="#">О нас</a>
        <a href="#">Услуги</a>
        <a href="#">Акции</a>
        <a href="#">Каталог</a>
        <a href="#">Контакты</a>
      </nav>
      <div className="hotline">телефон горячей линии (90)828-87-67</div>
    </header>

    <div className="banner">
      <h1>АВТОТЕХЦЕНТР</h1>
      <h2>СОВРЕМЕННЫЕ ТЕХНОЛОГИИ ОБСЛУЖИВАНИЯ - ГАРАНТИЯ КАЧЕСТВА!</h2>
      <h2>АКЦИЯ! ДИАГНОСТИКА ХОДОВОЙ ЧАСТИ БЕСПЛАТНО!</h2>
      <div className="form">
        <input type="text" placeholder="Имя" />
        <input type="text" placeholder="Телефон" />
        <button>Перезвонить мне</button>
      </div>
    </div>
  </div>
);

export default HomePage;
