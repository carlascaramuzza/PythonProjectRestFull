import { CampoEntradas } from "./entradas";
import { Container, StyledInput, StyledLabel } from "./styles";

export default function Campo({ label, propriedade, layout, tipo, larguraInput, onChange } : CampoEntradas){
    return <Container layout={layout}>
                <StyledLabel>{ label }</StyledLabel>
                <StyledInput name={propriedade} layout={layout} type={tipo} largura={larguraInput} onChange={onChange}/>
           </Container>
}