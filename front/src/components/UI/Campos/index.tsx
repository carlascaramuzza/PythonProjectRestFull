import { CampoEntradas } from "./entradas";
import { Container, StyledInput, StyledLabel } from "./styles";

export default function Campo({ label, layout, tipo, larguraInput } : CampoEntradas){
    return <Container layout={layout}>
                <StyledLabel>{ label }</StyledLabel>
                <StyledInput layout={layout} type={tipo} largura={larguraInput}/>
           </Container>
}