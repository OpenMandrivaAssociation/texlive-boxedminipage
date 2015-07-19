# revision 17087
# category Package
# catalog-ctan /macros/latex/contrib/boxedminipage
# catalog-date 2010-02-23 16:09:16 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-boxedminipage
Version:	20100223
Release:	10
Summary:	A package for producing framed minipages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/boxedminipage
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boxedminipage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX package which defines the boxedminipage environment --
like minipage, but with a frame around it.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/boxedminipage/boxedminipage.sty
%doc %{_texmfdistdir}/doc/latex/boxedminipage/boxedminipage.pdf
%doc %{_texmfdistdir}/doc/latex/boxedminipage/boxedminipage.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100223-2
+ Revision: 749869
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100223-1
+ Revision: 717976
- texlive-boxedminipage
- texlive-boxedminipage
- texlive-boxedminipage
- texlive-boxedminipage
- texlive-boxedminipage

