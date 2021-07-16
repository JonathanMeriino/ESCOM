-- Tipo C
library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;
entity hola is port(
	clk: in std_logic;                
	
	act: out std_logic_vector(3 downto 0));
	
							
end hola;
architecture holas of hola is
type estado is (E0,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15);
signal presente, futuro: estado;
 begin

	proceso_clk: 
	process (clk) begin
		if (clk'event and clk='1') then
			presente <= futuro;
		end if;
	end process proceso_clk;

	process (presente) begin
	case presente is
	
	when E0 =>
			futuro <= E1;
			act <= "1110";
	when E1 =>
			futuro <= E2;
			act <= "1110";
	when E2=>
			futuro <= E3;
			act <= "1101";
			
	when E3 =>
			futuro <= E4;
			act <= "1110";
			
	when E4 =>
			futuro <= E5;
			act <= "1101";
			
	when E5 =>
			futuro <= E6;
			act <= "1011";
		
	when E6 =>
			futuro <= E7;
			act <= "1110";
			
	when E7 =>
			futuro <= E8;
			act <= "1101";
			
	when E8 =>
			futuro <= E9;
			act <= "1011";
			
	when E9 =>
			futuro <= E10;
			act <= "0111";
			
	when E10 =>
			futuro <= E11;
			act <= "1101";
			
	when E11 =>
			futuro <= E12;
			act <= "1011";
			
	when E12 =>
			futuro <= E13;
			act <= "0111";
			
	when E13 =>
			futuro <= E14;
			act <= "1011";
	when E14 =>
			futuro <= E15;
			act <= "0111";
	when E15 =>
			futuro <= E0;
			act <= "0111";
			
	end case;
	end process;
end holas;