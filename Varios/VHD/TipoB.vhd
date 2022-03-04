-- Tipo B
library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;

entity hola is port(
	clk: in std_logic;                 
	sal: out std_logic_vector(3 downto 0));
end hola;

architecture holas of hola is
type estado is (E0, E1, E2, E3);
signal presente, futuro: estado;
 begin

	proceso_clk: 
	process (clk) begin
		if (clk'event and clk='1') then
			presente <= futuro;
		end if;
	end process proceso_clk;

	proceso_h: process (presente) begin
	case presente is
	when E0 =>
				futuro <= E1;
				sal <= "0111";
	when E1 =>
				futuro <= E2;
				sal <= "1011";
	when E2 =>
				futuro <= E3;
				sal <= "1101";
	when E3 =>
				futuro <= E0;
				sal <= "1110";
	end case;
	end process proceso_h;
end holas;