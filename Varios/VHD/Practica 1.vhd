library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;
entity dado1 is port(
	--clk: in std_logic;                 --clk=clok y X -> es una habilitacion
	z: in std_logic_vector (3 downto 0);
	L: out std_logic_vector(6 downto 0)); --letra
end dado1;
architecture a_dado of dado1 is
 begin

	proceso: process (z) begin
	case z is
	when "0111" =>
				L <= "0110111";--H
	when "1011" =>
				L <= "1111110";--O
	when "1101" =>
				L <= "0001110";--L
	when "1110" =>
				L <= "1110111";--A
	when others=>  --estados prohibidos
				L <= "0110111";--H
	end case;
	end process proceso;
end a_dado;

library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;
entity dado is port(
	clk: in std_logic;                 --clk=clok y X -> es una habilitacion
	z: out std_logic_vector(3 downto 0));
end dado;
architecture a_dado of dado is
type estados is (H, O, L, A);
signal edo_presente, edo_futuro: estados;
 begin

	proceso1: 
	process (clk) begin
		if (clk'event and clk='1') then
			edo_presente <= edo_futuro;
		end if;
	end process proceso1;

	proceso2: process (edo_presente) begin
	case edo_presente is
	when H =>
				edo_futuro <= O;
				z <= "0111";
	when O =>
				edo_futuro <= L;
				z <= "1011";
	when L =>
				edo_futuro <= A;
				z <= "1101";
	when A =>
				edo_futuro <= H;
				z <= "1110";
	end case;
	end process proceso2;
end a_dado;