import { css, Global } from "@emotion/react";
import Background from "./assets/background-navegacao.png";

function GlobalStyle(){
    return (
        <Global
            styles={css`
                body {
                    margin: 0;
                    padding: 0;
                    height: 100%;
                    width: 100%;
                    font-family: 'Josefin Sans, Allison';
                    background-image: url(${Background});
                    background-repeat: no-repeat;
                    background-size: cover;
                }
            `}
        />
    );
}

export default GlobalStyle;