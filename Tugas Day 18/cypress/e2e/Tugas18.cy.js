describe('template spec', () => {
  it('Positive Login', () => {
    cy.visit('https://the-internet.herokuapp.com/login')
    cy.get('#username').type('tomsmith')
    cy.wait(5)
    cy.get('#password').type('SuperSecretPassword!')
    cy.wait(5)
    cy.get('.fa').click()
    cy.wait(10)
    cy.get('.subheader').should('be.visible')
  })
})

describe('template spec', () => {
  it('Negative Login', () => {
    cy.visit('https://the-internet.herokuapp.com/login')
    cy.get('#username').type('tom')
    cy.get('#password').type('Super')
    cy.get('.radius').click()
    cy.get('#flash').should('be.visible')
  })
})