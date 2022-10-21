import { styled as materialStyled } from "@mui/material";
import Box from '@mui/material/Box';

export const CardConteudo = materialStyled(Box)(({ theme }) => ({
    backgroundColor: 'rgba(217, 217, 217, 0.9)',
    margin: '10px 0px',
    padding: '8px',
    height: '329px',
    width: '884px',
    overflow: 'auto',
    '& h6': {
        fontFamily: 'Josefin Sans',
        fontStyle: 'normal',
        fontWeight: 700,
        fontSize: '20px',
        lineHeight: '20px',
        marginBottom: '10px',
        marginTop: '5px'
    },
    '& span': {
        fontFamily: 'Josefin Sans',
        fontStyle: 'normal',
        fontWeight: 400,
        fontSize: '20px',
        lineHeight: '20px',
        margin: '5px 0px'
    },
    '& p': {
        fontFamily: 'Josefin Sans',
        fontStyle: 'normal',
        fontWeight: 300,
        fontSize: '20px',
        lineHeight: '20px'
    }
}));