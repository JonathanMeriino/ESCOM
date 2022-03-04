--- Tipo D
library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;
entity hola is port(
	clk: in std_logic;                 
	letra: out std_logic_vector(3 downto 0)); 
							
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
			letra <= "1000"; 
	when E1 =>
			futuro <= E2;
			letra <= "0100";
	when E2=>
			futuro <= E3;
			letra <= "1000";
	when E3 =>
			futuro <= E4;
			letra <= "0010";
	when E4 =>
			futuro <= E5;
			letra <= "0100";
	when E5 =>
			futuro <= E6;
			letra <= "1000"; 
	when E6 =>
			futuro <= E7;
			letra <= "0001";
	when E7 =>
			futuro <= E8;
			letra <= "0010";
	when E8 =>
			futuro <= E9;
			letra <= "0100";
	when E9 =>
			futuro <= E10;
			letra <= "1000";
	when E10 =>
			futuro <= E11;
			letra <= "0001"; 
	when E11 =>
			futuro <= E12;
			letra <= "0010";
	when E12 =>
			futuro <= E13;
			letra <= "0100";
	when E13 =>
			futuro <= E14;
			letra <= "0001";
	when E14 =>
			futuro <= E15;
			letra <= "0010";
	when E15 =>
			futuro <= E0;
			letra <= "0001"; 
	end case;
	end process;
end holas;