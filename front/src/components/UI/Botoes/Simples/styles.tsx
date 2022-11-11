import Button from "@mui/material/Button";
import { styled as materialStyled } from "@mui/material";

interface BotaoEntradas{
    largura: string;
}
export const Botao = materialStyled(Button)<BotaoEntradas>(({ largura, theme }) => ({
    backgroundColor: '#FFFFFF',
    borderRadius: '10px',
    fontFamily: 'Josefin Sans',
    fontStyle: 'italic',
    fontWeight: 400,
    fontSize: '20px',
    textTransform: 'initial',
    color: 'black',
    lineHeight: '20px',
    display: 'flex',
    alignItems: 'center',
    textAlign: 'center',
    width: largura,
    margin: "0px 5px",
    '&:hover': {
        backgroundColor: '#FFFFFF'
    }
}));