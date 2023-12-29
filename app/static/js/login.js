let loginDisplay = document.querySelector('.login-form')
let signupDisplay = document.querySelector('.signup-form')
let loginButton = document.querySelector('#login')
let signupButton = document.querySelector('#signup')

const m3 = (elem1, elem2, btn1, btn2) => {
    elem1.style.display = 'none'
    elem2.style.display = 'block'
    btn1.style.textShadow = '0 0 .5em #fff'
    btn2.style.textShadow = 'none'
}

const switchLogin = (bool) =>  {
    !bool ? m3(loginDisplay, signupDisplay, signupButton, loginButton) :
        m3(signupDisplay, loginDisplay, loginButton, signupButton)
}
