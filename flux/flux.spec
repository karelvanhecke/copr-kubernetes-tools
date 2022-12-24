%global goipath github.com/fluxcd/flux2
Version: 0.38.2

%global gomodulesmode GO111MODULE=on

%gometa

%global commit0 f58b82fb4ed53939dc1c9d7e370deab885527368
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: flux
Release: 1%{?dist}
Summary: Open and extensible continuous delivery solution for Kubernetes. Powered by GitOps Toolkit.
License: Apache-2.0
URL: %{gourl}
Source0: %{gosource}

BuildRequires: kustomize
BuildRequires: make

%description
%{summary}

%prep
%goprep -k

%build
export EMBEDDED_MANIFESTS_TARGET=cmd/flux/.manifests.done
make $EMBEDDED_MANIFESTS_TARGET
export LDFLAGS="-X main.VERSION=%{version} "
%gobuild -o %{gobuilddir}/bin/flux %{goipath}/cmd/flux

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md MAINTAINERS CODE_OF_CONDUCT.md CONTRIBUTING.md
%{_bindir}/*

%changelog
* Sat Dec 24 2022 Karel Van Hecke <copr@karelvanhecke.com> - 0.38.2-1
- Initial build
