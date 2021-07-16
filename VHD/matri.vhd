library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;

entity matricula is port(
	
	clk,switc: in std_logic;                 
	numero: out std_logic_vector(2 downto 0));
	
end matricula;

architecture matriculas of matricula is

type estado is (Esta1, Esta2, Esta3, Esta4, Esta5);
signal presente, futuro: estado;
 begin

	proceso_clk: --32574
	process (clk) begin
		if (clk'event and clk='1') then
			presente <= futuro;
		end if;
	end process proceso_clk;

	procesom: process (presente, numero) begin
	case presente is
	when Esta1 =>
			if switc = '1' then
				numero <= "010";--2
				futuro <= Esta2;

			else
				numero <= "011";--3
				futuro <= Esta1;

			end if;
	when Esta2 =>
			if switc = '0' then
				numero <= "101";--5
				futuro <=Esta3;

			else
				numero <= "010";--2
				futuro <= Esta2;

			end if;
	when Esta3 =>
			if switc = '1' then
				numero <= "111";--7
				futuro <= Esta4;

			else
				numero <= "101";--5
				futuro <= Esta3;

			end if;
	when Esta4 =>
			if switc = '1' then
				numero <= "100";--4
				futuro <= Esta5;

			else
				numero <= "111";--7
				futuro <= Esta4;

			end if;
	when Esta5 =>
			if switc = '1' then
				numero <= "011";--3
				futuro <= Esta1;

			else
				numero <= "100"; --4
				futuro <= Esta5;

			end if;
	when others =>
	numero <="000";
	 		

	end case;
	end process procesom;
end matriculas;
