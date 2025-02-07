%define luarocks_pkg_name base64
%define luarocks_pkg_version 1.5-3
%define luarocks_pkg_prefix base64-1.5-3
%define luarocks_pkg_major 1.5
%define luarocks_pkg_minor 3

Name: lua-base64
Version: 0
%define version1 %(echo %{version} 's/.*\\./-/' )
Release: %{luarocks_pkg_minor}
Summary: Pure Lua base64 encoder/decoder
Url: https://github.com/iskolbin/lbase64
License: MIT/Public Domain
Source0: base64-%{version1}.tar.gz
Source1: https://github.com/iskolbin/lbase64/blob/master/rockspec/base64-%(echo %{version} | sed 's/\\(.*\\)\\./\\1-/').rockspec
BuildRequires: lua-rpm-macros
Requires(postun): alternatives
Requires(post): alternatives
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
Pure Lua base64 encoder/decoder. Works with Lua 5.1+ and LuaJIT. Fallbacks to pure Lua bit operations if bit/bit32/native bit operators are not available.

%prep
%autosetup -p1 -n %{luarocks_pkg_prefix}
%luarocks_prep

%generate_buildrequires
%{?luarocks_buildrequires_echo}
%if %{with check}
%luarocks_generate_buildrequires -c -b
%else
%luarocks_generate_buildrequires -b 
%endif

%build
%{?custom_build}
%if %{defined luarocks_subpackages_build}
%{luarocks_subpackages_build}
%else
%if %{defined luarocks_pkg_build}
%luarocks_pkg_build %{lua_version}
%else
%luarocks_build --local
%endif
%endif

%install
%{?custom_install}
%if %{defined luarocks_subpackages_install}
%{luarocks_subpackages_install}
%else
%if %{defined luarocks_pkg_install}
%luarocks_pkg_install %{lua_version}
%else
%luarocks_install %{luarocks_pkg_prefix}.*.rock
%endif
%endif
%{?lua_generate_file_list}

%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}
