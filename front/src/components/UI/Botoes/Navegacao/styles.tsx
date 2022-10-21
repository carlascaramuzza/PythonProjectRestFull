import Button from "@mui/material/Button";
import { styled as materialStyled } from "@mui/material";

export const Botao = materialStyled(Button)(({ theme }) => ({
    backgroundColor: 'rgba(217, 217, 217, 0.9)',
    borderRadius: '15px',
    margin: '10px 0px',
    fontFamily: 'Allison',
    fontStyle: 'normal',
    fontWeight: 400,
    fontSize: '60px',
    textTransform: 'initial',
    color: 'black',
    lineHeight: '76px',
    '&:hover': {
        backgroundColor: 'rgba(217, 217, 217, 0.9)'
    }
}));
