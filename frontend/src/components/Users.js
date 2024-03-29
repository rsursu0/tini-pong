import AbstractComponent from "./AbstractComponent.js";

export default class extends AbstractComponent {
	constructor() {
		super();
		this.setTitle("Users");
	}

	async getHtml(loginModule) {
		loginModule.isLogin();
		return `
		<h1>User Page</h1>
		<p>This is User Page.</p>
		`;
	}

	handleRoute() {

	}
}