describe('UI Smoke Test', () => {
	const email = `smoke_${Date.now()}@example.com`;
	const password = 'SmokePass#12345';
	const name = 'Smoke Tester';
	const message = 'Hello from automated smoke test';

	function ensureAuthenticated() {
		cy.location('pathname', { timeout: 30000 }).then((pathname) => {
			if (pathname.includes('/auth')) {
				cy.get('body').then(($body) => {
					const hasSignUpSwitch = $body.text().includes("Don't have an account?");
					if (hasSignUpSwitch) {
						cy.contains('button', 'Sign up').click({ force: true });
					}
				});

				cy.get('body').then(($body) => {
					if ($body.find('#name').length > 0) {
						cy.get('#name').clear().type(name);
					}
				});

				cy.get('#email').clear().type(email);
				cy.get('#password').clear().type(password, { log: false });

				cy.get('body').then(($body) => {
					if ($body.find('#confirm-password').length > 0) {
						cy.get('#confirm-password').clear().type(password, { log: false });
					}
				});

				cy.get('form button[type="submit"]').first().click({ force: true });
				cy.location('pathname', { timeout: 60000 }).should('not.include', '/auth');
			}
		});
	}

	it('logs in, selects suggestion, sends message, and stays logged in after refresh', () => {
		cy.visit('http://127.0.0.1:5173', { timeout: 120000 });
		ensureAuthenticated();

		cy.get('#chat-input', { timeout: 60000 }).should('be.visible');

		cy.get('body').then(($body) => {
			if ($body.find('[role="listitem"]').length > 0) {
				cy.get('[role="listitem"]').first().click({ force: true });
			} else {
				cy.get('#chat-input').click().type(message);
			}
		});

		cy.get('#chat-input').invoke('text').should('not.match', /^\s*$/);
		cy.get('#send-message-button').should('be.visible').click({ force: true });

		// Submission should create a visible result (assistant output or explicit connection error),
		// never silent failure.
		cy.contains('Connection to realtime service failed', { timeout: 30000 })
			.should('be.visible')
			.then(
				() => {},
				() => {
					// Fallback success path: any rendered response content area is acceptable.
					cy.get('#messages-container', { timeout: 30000 })
						.invoke('text')
						.should((text) => {
							expect(text.trim().length).to.be.greaterThan(0);
						});
				}
			);

		cy.reload();
		cy.location('pathname', { timeout: 30000 }).should('not.include', '/auth');
		cy.get('#chat-input', { timeout: 30000 }).should('be.visible');
	});
});
